# trading-psychology

Nhật ký và hồ sơ tâm lý giao dịch cá nhân — tài liệu tham khảo *Trading in the Zone* (Mark Douglas).

## Cấu trúc

```
.
├── README.md                              ← file này
├── CLAUDE.md                              ← hướng dẫn cho Claude khi làm việc trong thư mục
├── .gitignore
├── trading-psychology-profile.md          ← hồ sơ 30-câu khảo sát, chẩn đoán, lộ trình, nhật ký
└── book/
    ├── extract-pdf-to-md.py               ← script trích PDF → markdown (giữ lại để tái sử dụng)
    ├── Trading-in-the-zone-vi.md          ← (gitignored — bản quyền)
    └── Trading-in-the-zone-en.md          ← (gitignored — bản quyền)
```

## Nội dung

- **`trading-psychology-profile.md`** — kết quả khảo sát thái độ 30 câu (Chương 1 *Trading in the Zone*), chẩn đoán các mâu thuẫn cốt lõi trong tư duy giao dịch, lộ trình thực hành, và nhật ký phiên.
- **`book/extract-pdf-to-md.py`** — script Python dùng `pdfplumber` + `regex` để trích PDF sách bất kỳ ra markdown. Heading detection theo mẫu ALL CAPS ở đầu trang.

## Bắt đầu

```bash
git clone <repo-url>
# Đọc hồ sơ trước:
cat trading-psychology-profile.md
```

Khi bắt đầu phiên làm việc với AI (Claude), vào thư mục gốc và mở Claude Code — `CLAUDE.md` sẽ tự nạp.

## Ghi chú bản quyền

Các file markdown trong `book/` chứa nội dung trích từ *Trading in the Zone* © Mark Douglas, được giữ cục bộ cho mục đích học tập cá nhân và **không commit lên repo này**.

## License

Nội dung cá nhân trong repo thuộc về tác giả (hieuphan94). Mã nguồn script trong `book/` có thể dùng lại tự do.
