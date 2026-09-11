# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> temperature tăng thì độ sáng tạo câu trả lời tăng. Càng thấp câu trả lời càng ổn định tập trung.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Đặt temperature thấp cho chatbot (~0.2), vì câu trả lời cần sự nhất quán và không lan man đồng thời vẫn đủ ngữ điệu tự nhiên khi giao tiếp, để quá cao gây ra sự khó chịu thông tin cho khách hàng.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> Tổng sản lượng đầu ra mỗi ngày là: ~ 10.500.000 token

Theo bảng giá:

- GPT-4o: `10.500 × 0,010 = 105 USD/ngày`
- GPT-4o-mini: `10.500 × 0,0006 = 6,30 USD/ngày`

Vì vậy, GPT-4o đắt hơn khoảng 16,7 lần (chỉ tính token đầu ra). GPT-4o xứng đáng khi xử lý yêu cầu phức tạp, cần độ chính xác cao như tư vấn pháp lý hoặc phân tích chuyên sâu; nên dùng mini cho các tác vụ đơn giản, lặp lại như phân loại yêu cầu.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> - Phản hồi cho trẻ em thường ngắn, dùng từ đơn giản và ví dụ quen thuộc.Phản hồi chuyên gia thường dài hơn, dùng thuật ngữ. Hai câu trả lời có thể cùng giải thích một khái niệm nhưng khác nhau về mức độ chi tiết và cách diễn đạt. System prompt định hướng persona, đối tượng người đọc, từ vựng, độ sâu và loại ví dụ mà model sử dụng.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Số token đo bằng tiktoken là 172, trong khi cách ước lượng số từ chia cho 0.75 cho kết quả 182.67, chênh lệch khoảng 5%. Tiếng Việt thường tốn nhiều token hơn tiếng Anh vì cách tách token phụ thuộc vào dữ liệu huấn luyện và tiếng Việt có nhiều dấu, âm tiết và từ ghép. Một từ tiếng Việt đôi khi có thể bị chia thành nhiều token nhỏ hơn. Vì vậy, cách đếm từ chỉ mang tính ước lượng, còn tiktoken phản ánh gần hơn số token thực tế của model.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng khi cần phản hồi nhanh và tạo cảm giác hệ thống đang xử lý, chẳng hạn như chatbot, trợ lý ảo hoặc ứng dụng tạo văn bản dài. Người dùng có thể bắt đầu đọc kết quả ngay thay vì chờ toàn bộ nội dung hoàn tất. Ngược lại, non-streaming phù hợp hơn khi kết quả ngắn, cần xử lý toàn bộ trước khi hiển thị, hoặc khi ứng dụng yêu cầu dữ liệu hoàn chỉnh để thực hiện bước tiếp theo, như gọi API, trả về JSON hoặc thực hiện giao dịch.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff giúp giảm dần áp lực lên API bằng cách tăng thời gian chờ sau mỗi lần retry, tạo cơ hội để hệ thống phục hồi. Nếu hàng nghìn client cùng retry với delay cố định, chúng có thể gửi request lại đồng thời sau mỗi 1 giây, gây ra hiện tượng “thundering herd”, làm API tiếp tục quá tải và khiến lỗi lặp lại. Thực tế thường kết hợp thêm thời gian ngẫu nhiên nhỏ để phân tán các lần retry.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Persona chọn: Bạn là trợ giảng thân thiện của khóa học AI. Hãy giải thích các khái niệm rõ ràng, dễ hiểu và trả lời ngắn gọn bằng tiếng Việt. Khi phù hợp, hãy đưa ra ví dụ thực tế hoặc đoạn mã minh họa. Giải thích:
- “Trợ giảng thân thiện” giúp trợ lý có giọng điệu gần gũi, hỗ trợ người học thay vì trả lời quá máy móc.
- “Trả lời ngắn gọn bằng tiếng Việt” giúp câu trả lời dễ đọc, phù hợp với thời lượng học tập và đảm bảo người dùng hiểu nội dung bằng ngôn ngữ quen thuộc.
- Yêu cầu “đưa ra ví dụ thực tế hoặc đoạn mã minh họa” giúp các khái niệm AI và lập trình trực quan hơn.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế là history chỉ lưu tối đa 3 lượt hội thoại gần nhất. Vì vậy, trợ lý có thể quên những thông tin quan trọng đã trao đổi trước đó. Cải thiện cụ thể: triển khai bộ nhớ dài hạn bằng cách lưu các thông tin quan trọng vào cơ sở dữ liệu hoặc file JSON. Sau mỗi lượt trò chuyện, hệ thống sẽ tóm tắt và lưu các dữ kiện cần nhớ. Khi có câu hỏi mới, chương trình tìm lại các thông tin liên quan rồi đưa chúng vào system prompt hoặc messages trước khi gọi API.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
