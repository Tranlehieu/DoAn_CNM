# Thông tin về bài tập

## Đồ án phần mềm: ứng dụng Machine Learning(xx%) *[chi tiết](./DoAn)*

Xây dựng trang DashBoard phân tích trading theo các tiêu chí sau
1) Người dùng chọn một trong các phương pháp dự đoán:
    a. XGBoost, RNN, LSTM (bắt buộc) hoặc các phương pháp khác.
    b. Transformer and Time Embeddings(nâng cao - có thể làm hoặc không, có điểm cộng)
2) Người dùng chọn một hay nhiều đặc trưng để dự đoán :
    a. Close, ROC (bắt buộc)
    b. RSI, Bolling Bands, Moving Average,...(nâng cao)
    c. Đường hỗ trợ/kháng cự (nâng cao)
3) Hiển thị giá dự đoán của timeframe kế tiếp (visualize)
4) Lấy dữ liệu Real-time từ websocket của Binance, chứng khoán,...
    a. Lấy dữ liệu lớn hơn 1000 nến (candle) từ lịch sử
    b. Lấy dữ liệu real-time append vô dữ liệu hiện tại
    c. Dự đoán giá nến (candle) kế tiếp

Xây dựng DashBoard theo tutorial sau: https://data-flair.training/blogs/stock-price-prediction-machine-learning-project-in-python/

Tiêu chí chấm : Hỗ trợ càng nhiều mô hình dự đoán(Kết hợp phương pháp và các đặc trưng) càng tốt, giao diện đẹp, tiện dụng, dễ xài.

Lưu ý: ứng dụng được thêm các nội dung đã seminar vào sẽ được cộng thêm điểm.

## Bài tập cá nhân:

### Machine Learning

Thực hiện theo tutorial để làm quen với mô hình dự đoán và triển khai ứng dụng trên môi trường web.
Cặp tiền dự đoán: BTC-USD, ETH-USD, ADA-USD

Yêu cầu: Quay lại video demo sản phẩm

### Blockchain
Yêu cầu:
    - Ghi nhận quá trình làm việc lên Github (Source Code, Tài liệu tham khảo, Readme.txt)
    - Quay lại video cách sử dụng
    - Xây dựng hệ thống tiền điện tử MyCoin:

1. Phần giao diện và quá trình thao tác tương tự https://www.myetherwallet.com/wallet/create

    a. Tạo Ví(Wallet) : Private key/ Passphrase/....
    b. Xem thống kê tài khoản
    c. Gởi coin cho một địa chỉ khác
    d. Xem lịch sử giao dịch (build giống GUI https://etherscan.io/)

2. Sử dụng thuật toán Proof Of Stake