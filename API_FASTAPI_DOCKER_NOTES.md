# API, FastAPI và Docker Notes

## API

API là cách để một chương trình gọi chức năng hoặc lấy dữ liệu từ một chương trình khác

Một request API thường gồm:

- Method: hành động muốn thực hiện, ví dụ `GET`, `POST`, `PUT`, `DELETE`
- URL: địa chỉ endpoint, ví dụ `/api/predict/v2`
- Body: dữ liệu gửi lên server, thường dùng với `POST` hoặc `PUT`
- Response: kết quả server trả về, thường là JSOn

Các method hay dùng:

- `GET`: lấy dữ liệu.
- `POST`: gửi dữ liệu mới để server xử lý tác vụ hoặc tạo mới
- `PUT`: cập nhật dữ liệu
- `DELETE`: xóa dữ liệu
Còn có:
- `PATCH`: cập nhật một phần dữ liệu 

Ví dụ body JSON:

```json
{
  "image_path": "digit_8.png"
}
```

Ví dụ response JSON:

```json
{
  "predicted_class": 8,
  "confidence": 0.99
}
```

## API versioning

Versioning dùng để thay đổi API mà vẫn giữ client cũ chạy được

Ví dụ:

```text
POST /api/predict/v1
POST /api/predict/v2
```

`v1` có thể trả output đơn giản, còn `v2` có thể bổ sung thêm field mới như `confidence` hoặc `execution_time`

## FastAPI

FastAPI là framework Python để xây REST API nhanh và tiện

Các thành phần thường dùng:

- `FastAPI()`: tạo app chính.
- `APIRouter`: tách endpoint thành nhiều nhóm.
- `BaseModel`: định nghĩa schema request/response bằng pydantic
- `Depends`: inject dependency hoặc service vào endpoint
- `response_model`: khai báo format response trả ra

Ví dụ endpoint cơ bản:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    image_path: str

@app.post("/predict")
def predict(request: PredictRequest):
    return {"predicted_class": 8}
```

FastAPI tự sinh tài liệu API tại:

```text
http://localhost:8000/docs
```

Link này dùng để xem endpoint, schema và test API trực tiếp

## Postman

Postman dùng để test API thủ công

Các bước cơ bản:

- Chọn method như `GET` hoặc `POST`
- Nhập URL endpoint
- Nếu request cần body, chọn `Body -> raw -> JSON`
- Bấm Send để xem response


## Docker

Docker giúp đóng gói app cùng môi trường chạy vào container

Các khái niệm chính:

- Image: bản đóng gói được build từ Dockerfile
- Container: image đang được chạy
- Dockerfile: file mô tả cách build image
- Port mapping: nối port trong container ra port trên máy host

Các lệnh hay dùng:

```text
docker build -t app-name:latest .
docker run -d -p 8000:8000 --name app-container app-name:latest
docker ps
docker stop app-container
docker rm app-container
docker images
```

Ý nghĩa `-p 8000:8000`:

```text
host_port:container_port
```

Tức là khi truy cập `localhost:8000` trên máy thật, request sẽ được chuyển vào port `8000` trong container (a:b thì local giao tiếp với container ở port a còn các container khác giao tiếp với container được tạo ở port b)

## Dockerfile cơ bản

Ví dụ trong repo:

```dockerfile
FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
```

Ý nghĩa:

- `FROM`: chọn base image
- `COPY`: copy file từ máy vào image
- `RUN`: chạy lệnh khi build image
- `CMD`: lệnh mặc định khi container chạy
- `EXPOSE`: ghi chú port app sẽ dùng trong container

