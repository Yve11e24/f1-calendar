# F1 Calendar

一個使用 Python 製作的 2026 F1 賽程行事曆工具。

## 功能

- 自動取得 2026 F1 賽程
- 取得練習、Sprint、排位賽與正賽
- 將 UTC 時間轉換成台灣時間
- 自動計算各 Session 的結束時間
- 產生 `.ics` 行事曆檔案
- 可以將 `.ics` 匯入支援行事曆檔案的行事曆 App

## 使用技術

- Python
- Requests
- F1 API
- JSON
- datetime
- iCalendar

## 如何使用

### 1. 安裝 Python

請先安裝 Python。

### 2. 安裝 requests

在終端機執行：

```bash
pip install requests