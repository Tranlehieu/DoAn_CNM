# Đồ án phần mềm: ứng dụng Machine Learning

Xây dựng trang DashBoard phân tích trading theo các tiêu chí sau
1) Người dùng chọn một trong các phương pháp dự đoán:
    a. XGBoost, RNN, LSTM (bắt buộc) hoặc các phương pháp khác. -> Đã làm
    b. Transformer and Time Embeddings(nâng cao - có thể làm hoặc không, có điểm cộng) -> Không có
2) Người dùng chọn một hay nhiều đặc trưng để dự đoán :
    a. Close, ROC (bắt buộc) -> Đã làm
    b. RSI, Bolling Bands, Moving Average,...(nâng cao) -> Không có
    c. Đường hỗ trợ/kháng cự (nâng cao) -> Không có
3) Hiển thị giá dự đoán của timeframe kế tiếp (visualize)
4) Lấy dữ liệu Real-time từ websocket của Binance, chứng khoán,...
    a. Lấy dữ liệu lớn hơn 1000 nến (candle) từ lịch sử -> Đã làm
    b. Lấy dữ liệu real-time append vô dữ liệu hiện tại -> Không có
    c. Dự đoán giá nến (candle) kế tiếp -> Đã làm