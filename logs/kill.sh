#!/bin/bash

# 指定目录路径
DIRECTORY="."  # 请替换为实际目录路径

# 使用 lsof 命令获取指定目录下所有 .nfs 文件的PID
PIDS=$(lsof +D "$DIRECTORY" | grep '\.nfs' | awk '{print $2}' | sort | uniq)

if [ -z "$PIDS" ]; then
    echo "No .nfs files found or no PIDs to kill."
    exit 0
fi

# 终止这些PID对应的进程
for PID in $PIDS; do
    kill -9 "$PID" && echo "Successfully killed PID: $PID" || echo "Error killing PID: $PID"
done