# BigData_Lab1: Thực hành tổng hợp HDFS và MapReduce Streaming

## 1. Giới thiệu

Bài toán: một đơn vị có dữ liệu giao dịch theo chi nhánh. Bài thực hành đưa dữ liệu lên HDFS, kiểm tra cấu trúc lưu trữ và thực hiện một bài toán tổng hợp đơn giản: **tính tổng số tiền (Amount) theo từng chi nhánh (Branch)** bằng Hadoop MapReduce Streaming (Python).

- **Môi trường:** Google Colab, Java 8, Hadoop 3.5.0 (chế độ pseudo-distributed, 1 máy)
- **Sinh viên thực hiện:** ...
- **Lớp / Môn học:** ...

## 2. Cấu trúc thư mục

```
BigData_Lab1/
├── README.md
├── HDFS_Lab.ipynb        # Notebook Colab chứa toàn bộ các bước
├── transactions.txt      # Dữ liệu đầu vào (>= 20 dòng)
├── mapper.py             # Mapper của MapReduce Streaming
├── reducer.py            # Reducer của MapReduce Streaming
├── output/               # Kết quả tải từ HDFS về (_SUCCESS, part-00000)
└── screenshots/          # Ảnh/log minh chứng các lệnh kiểm chứng
```

## 3. Dữ liệu đầu vào

File `transactions.txt` gồm 30 dòng, mỗi dòng theo cấu trúc:

```
Branch,TransactionType,Amount
```

Ví dụ: `Hanoi,Deposit,1500`

## 4. Các bước thực hiện

| Bước | Nội dung | Lệnh chính |
|------|----------|-----------|
| 1 | Tạo `transactions.txt` trên Colab (>= 20 dòng) | Python sinh dữ liệu ngẫu nhiên, `cat` để kiểm tra |
| 2 | Tạo thư mục trên HDFS | `hdfs dfs -mkdir -p /user/student/transactions/input` |
| 3 | Đưa file lên HDFS và chứng minh | `hdfs dfs -put`, `hdfs dfs -ls`, `hdfs dfs -cat` |
| 4 | Xác định số block và vị trí block | `hdfs fsck <file> -files -blocks -locations` |
| 5 | Ghi nhận dung lượng | `hdfs dfs -du -h`, `hdfs dfsadmin -report` |
| 6 | Chạy MapReduce Streaming, đầu ra ghi về HDFS | `hadoop jar hadoop-streaming-3.5.0.jar ...` |
| 7 | Tải kết quả từ HDFS về `/content` | `hdfs dfs -get /user/student/transactions/output /content/output` |
| 8 | Nộp ảnh/log kiểm chứng | Xem thư mục `screenshots/` |

### Bước 6: Bài toán MapReduce

- **Mapper** (`mapper.py`): đọc từng dòng, tách theo dấu phẩy, xuất `Branch<TAB>Amount`.
- **Reducer** (`reducer.py`): cộng dồn Amount theo từng Branch (dữ liệu đã được sắp xếp theo key), xuất `Branch<TAB>Tổng`.

Lệnh chạy:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
  -files /content/mapper.py,/content/reducer.py \
  -mapper mapper.py -reducer reducer.py \
  -input /user/student/transactions/input \
  -output /user/student/transactions/output
```

## 5. Kết quả

Tổng Amount theo chi nhánh (nội dung `output/part-00000`):

```
(dán kết quả cat /content/output/part-* vào đây)
```

Thông tin lưu trữ ghi nhận từ `fsck` và `dfsadmin`:

- Số block của `transactions.txt`: ...
- Vị trí block (DataNode): ...
- Dung lượng file (`du -h`): ...

## 6. Ảnh minh chứng (bước 8)

| Lệnh | Ảnh |
|------|-----|
| `jps` | ![jps](screenshots/jps.png) |
| `hdfs dfsadmin -report` | ![dfsadmin](screenshots/dfsadmin_report.png) |
| `hdfs dfs -ls` | ![ls](screenshots/ls.png) |
| `hdfs dfs -cat` | ![cat](screenshots/cat.png) |
| `hdfs fsck` | ![fsck](screenshots/fsck.png) |
| Output bài xử lý | ![output](screenshots/output.png) |

## 7. Cách chạy lại

1. Mở `HDFS_Lab.ipynb` trên Google Colab.
2. Chạy lần lượt các cell từ trên xuống (cài Java và Hadoop, cấu hình, khởi động NameNode/DataNode, rồi các bước 1 đến 7).
3. Lưu ý: khi Colab reset runtime thì HDFS bị xóa, cần chạy lại từ đầu.
