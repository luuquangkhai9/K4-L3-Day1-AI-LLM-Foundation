from template import count_tokens, OPENAI_MODEL

text = """
Blockchain là một công nghệ lưu trữ dữ liệu theo dạng chuỗi các khối liên kết với nhau.
Mỗi khối chứa thông tin giao dịch và được bảo vệ bằng kỹ thuật mã hóa.
Dữ liệu được lưu trên nhiều máy tính trong cùng một mạng lưới nên rất khó bị thay đổi.
Nhờ đó, blockchain có thể tạo ra sự minh bạch và tin cậy mà không cần một trung tâm
kiểm soát duy nhất. Công nghệ này được sử dụng phổ biến trong tiền điện tử, nhưng
cũng có thể áp dụng cho ngân hàng, quản lý chuỗi cung ứng, y tế, giáo dục và nhiều
lĩnh vực khác. Người dùng có thể kiểm tra lịch sử giao dịch, trong khi hệ thống vẫn
bảo đảm tính toàn vẹn và an toàn của dữ liệu.
"""

word_count = len(text.split())
estimated_tokens = word_count / 0.75
actual_tokens = count_tokens(text, model=OPENAI_MODEL)

difference_percent = (
    abs(actual_tokens - estimated_tokens) / estimated_tokens * 100
)

print(f"Số từ: {word_count}")
print(f"Token theo tiktoken: {actual_tokens}")
print(f"Token ước lượng: {estimated_tokens:.2f}")
print(f"Chênh lệch: {difference_percent:.2f}%")