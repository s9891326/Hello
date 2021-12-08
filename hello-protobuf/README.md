# 程式碼所在目錄
SRC_DIR=`pwd`

# 輸出目錄
DST_DIR=`pwd`

# 編譯 .proto 檔
protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto

./build
