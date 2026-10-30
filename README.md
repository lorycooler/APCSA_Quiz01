# APCSA Java Practice Lab — v1

直接以瀏覽器開啟 `index.html`。離線、純靜態、無登入及資料庫，不讀寫 localStorage 或 sessionStorage。

## 題庫配置

四個單元：Using Objects and Methods、Selection and Iteration、Class Creation、Data Collections。

每單元填空 2 份 × 20 題，選擇 5 份 × 16 題；共 28 份、480 題。排除繼承與多型。每題提交後立即公布答案及解析，完成整份後以答對比例計算百分制成績並四捨五入。

內容包括 12 題經來源答案核對的 CB PDF 原題重新排版，以及 468 題依題庫主題編寫的填空與選擇改編題。不同選擇題份數包含同一概念的情境與數值變式，不應描述為 480 道互不相關的官方原題。每題均有來源類型說明。

## 擴充與修改

1. 編輯 `bank.json` 的 `questions`。每題保留唯一 `id`，指定 `unit`、`type`（fill/mcq）及 `set`。
2. 新增第 6 份選擇題時，新增同一 unit 下 `set: 6` 的 16 道題；不必修改選單程式，選單會依題庫資料自動增加。
3. 填空題以 `___` 標記空格，`answers` 為「每一空的可接受答案陣列」。例如 `[["int"]]`、`[["mid + 1", "1 + mid"]]`。Java 大小寫與運算子邊界會影響判分；程式不執行學生輸入。
4. 選擇題 `options` 固定 4 項，`answer` 為對應的 A/B/C/D；更換選項順序須同步修改答案。
5. 保留 `prompt`、`code`、`explanation`、`source`，明確區分原題、改編與自編，新增題目須另外核對答案。
6. 執行 `python render_site.py`，即可重新產生 `index.html`。也可加 `--output 自訂檔名.html`。只需 Python 標準函式庫，不需 Java、Node 或 PDF 工具。

請勿直接修改 `index.html` 內嵌資料後又從舊 `bank.json` 重建；以 `bank.json` 為題庫主檔。

## 上傳 GitHub Pages

網站只需要 `index.html`。維護檔可放在儲存庫，原始 PDF、書籍及工具暫存目錄不需上傳。網站首頁為 index.html。GitHub Pages 可使用 main 分支的 / (root) 發布。

## 驗證紀錄

- 瀏覽器逐題測試 480 題、28 份題組，檢查答案鎖定、空白輸入、所有單元入口、計分、重新整理清除狀態與手機版無水平溢出。
- 248 道可直接執行的選擇題，以 Java 21 編譯執行並核對輸出，全數通過；其餘為概念、編譯條件與語法填空，未宣稱全部題目經 Java 執行驗證。
- 新增題目後需重新核對與測試，現有驗證紀錄不涵蓋後續修改。

