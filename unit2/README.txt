SKYLINE KIDS — UNIT 2: My Family (/f/ /m/)
==========================================

NỘI DUNG ZIP NÀY
- u2cover.html, u2s1..s5.html  : 6 màn hình bài học (up lên Cloudflare Pages: klis-skyline.pages.dev)
- Unit2_Quizzes_FINAL_Import_Ready.zip : 4 quiz Moodle (Gate2/3/4 + Final) — import vào Moodle Question bank
- Skyline_Speaking_Rubric.md       : rubric chấm speaking (dùng chung mọi unit, 15%)
- unit_data_U2.py                 : toàn bộ nội dung unit (sửa ở đây rồi build lại)

DEPLOY (tóm tắt)
1. Up 6 file HTML + toàn bộ asset (ảnh/audio/video, ~~30 file) lên klis-skyline.pages.dev
   (đảm bảo đã up file _headers cho CORS — xem SOP).
2. Trong Moodle: tạo URL resource trỏ tới mỗi HTML (Display = Open).
3. Import 4 quiz XML; tạo Speaking Assignment + gắn rubric; đặt Activity Completion + Restrict Access.
4. Dán link Moodle Final quiz vào field 'final_url' trong unit_data_U2.py rồi build lại u2s5.html
   (hoặc sửa trực tiếp var FINAL_URL trong u2s5.html).

BUILD LẠI
   python3 build_unit_GENERATOR_v3.py   (sau khi import UNIT từ unit_data_U2.py)
   Cần engine + kit (xem gói _ENGINE).

TÍNH NĂNG: vocab cards + match game + memory game (lật thẻ) · story karaoke (sáng từng từ)
           · grammar builder ép đúng thứ tự · phonics unlock · speaking 3 cấp + checklist.
