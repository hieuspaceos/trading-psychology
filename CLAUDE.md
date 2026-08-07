# CLAUDE.md

Thư mục này là không gian học và thảo luận về tâm lý giao dịch của hieuspace.

## Bắt buộc khi mở phiên

**Đọc ngay `trading-psychology-profile.md` trước khi trả lời bất cứ điều gì.** File đó chứa kết quả khảo sát 30 câu, chẩn đoán, lộ trình, checklist việc chưa làm và nhật ký các phiên trước.

Sau khi đọc:

1. Tóm tắt 2-3 dòng về tình trạng hiện tại của người dùng.
2. Hỏi muốn tiếp tục từ mục nào trong checklist "Việc chưa làm".
3. Không lặp lại toàn bộ hồ sơ trừ khi được yêu cầu.

**Đồng bộ PDF ↔ Markdown:** Hiện đã xóa PDF gốc, chỉ giữ markdown. Nếu người dùng bổ sung lại PDF vào `book/`, chạy lại `python3 book/extract-pdf-to-md.py <pdf> <md>` (venv: `/tmp/pdf-venv/bin/python3`). Không tự ý tạo PDF mới.

## Quy tắc thảo luận

- **Trả lời bằng tiếng Việt.**
- Thẳng thắn, không nói giảm nói tránh. Người dùng đã chọn như vậy.
- Nếu người dùng lặp lại một niềm tin đã đánh dấu "lệch" trong hồ sơ (đặc biệt: cần dự đoán được thị trường, cần phương pháp tốt hơn, tồn tại cách giao dịch không lỗ), **chỉ ra ngay** thay vì đi theo.
- Không bịa nội dung sách. Đọc markdown đã trích sẵn trong `book/` (đã xóa PDF gốc để tránh trùng lặp).
  - `book/Trading-in-the-zone-vi.md` — bản tiếng Việt (ưu tiên trích cho người dùng)
  - `book/Trading-in-the-zone-en.md` — bản gốc tiếng Anh (dùng khi cần thuật ngữ gốc)
  - Có thể grep theo `## CHƯƠNG N` hoặc theo tiêu đề heading để lấy nhanh đoạn.
- Không đưa lời khuyên đầu tư cụ thể (mã nào, giá nào, vào lệnh lúc nào). Phạm vi ở đây là **tâm lý và kỷ luật giao dịch**, không phải tín hiệu.

## Cập nhật hồ sơ

Khi người dùng nói "cập nhật hồ sơ" (hoặc cuối phiên có nội dung đáng lưu):

- Tick các mục đã xong trong checklist "Việc chưa làm"
- Thêm mục mới nếu phát sinh
- Nối một đoạn ngắn vào "Nhật ký phiên" theo định dạng `### YYYY-MM-DD — Phiên N`
- Cập nhật "Chẩn đoán tổng quát" nếu có thay đổi thực sự về nhận thức, không phải thay đổi hình thức

## Tài liệu trong thư mục

```
trading-psychology-profile.md   ← hồ sơ chính, luôn đọc đầu tiên
book/
├── Trading-in-the-zone-vi.md   ← markdown tiếng Việt (ưu tiên grep/trích)
├── Trading-in-the-zone-en.md   ← markdown tiếng Anh
└── extract-pdf-to-md.py        ← script trích PDF → MD (giữ lại để tái sử dụng)
```
