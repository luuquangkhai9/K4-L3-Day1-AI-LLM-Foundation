from template import chat_with_system_prompt

question = "Giải thích blockchain là gì?"

simple_answer, _ = chat_with_system_prompt(
    "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi.",
    question,
)

expert_answer, _ = chat_with_system_prompt(
    "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật.",
    question,
)

print("Phản hồi dành cho trẻ em:")
print(simple_answer)

print("\nPhản hồi chuyên gia:")
print(expert_answer)