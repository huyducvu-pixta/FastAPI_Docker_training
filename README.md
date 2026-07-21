# MNIST Model API

Repo demo một API nhận diện chữ số viết tay MNIST bằng FastAPI.

## API thực hiện gì

API cho phép:

- Xem danh sách model có sẵn: `mlp`, `cnn`.
- Chọn model đang được deploy để inference.
- Gửi ảnh chữ số mẫu và nhận kết quả dự đoán.
- Xem, lấy chi tiết và xóa lịch sử prediction.

Ví dụ request predict version 1:

```text
POST /api/predict/v1
```

```json
{
  "image_path": "digit_0.png"
}
```

API sẽ trả về class dự đoán:

```json
{
  "predicted_class": 0
}
```

Ví dụ request predict version 2:

```text
POST /api/predict/v2
```

API sẽ trả về class dự đoán, confidence và thời gian chạy:

```json
{
  "predicted_class": 0,
  "confidence": 0.9999945163726807,
  "execution_time": 0.0123
}
```

## Repo gồm những phần:

- `app/main.py`: khởi tạo FastAPI app và đăng ký router
- `app/api/routers/`: định nghĩa các endpoint cho models, deploy và predict
- `app/schemas/`: định nghĩa request/response bằng pydantic
- `app/services/`: xử lý logic load model, deploy model và inference
- `app/models/`: kiến trúc model `MLP` và `CNN`
- `app/model_weights/`: trọng số model đã train
- `app/notebooks/`: notebook train model
- `app/test_samples/`: ảnh MNIST mẫu để test API

## Docker thực hiện:

Docker  đóng gói API và môi trường chạy vào một container.

Khi build Docker image, docker thực hiện: 

- Cài Python và các thư viện trong `requirements.txt`.
- Copy source code, model weights,... vào image.
- Chạy FastAPI 
- Mở port `8000` để gọi API từ Postman để check.

Lệnh build image:
```text
docker build -t mnistapi:latest .  
```

Lệnh run container:
```text
docker run -d -p 8000:8000 --name fastapi-mnist mnistapi 
```
## Thông tin thêm:
Có thể check OpenAPI tại:

```text
http://localhost:8000/docs
```

Postman test exported file:


```text
Test MNIST API.postman_collection.json
```
