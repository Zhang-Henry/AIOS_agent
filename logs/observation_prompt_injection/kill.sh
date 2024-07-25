#!/bin/bash

# 读取当前目录下的所有 .nfs 文件
nfs_files=$(find . -type f -name ".nfs*")

# 遍历每个 .nfs 文件
for file in $nfs_files; do
  # 使用 lsof 获取正在使用该文件的进程的 PID
  pids=$(lsof $file | awk 'NR>1 {print $2}')

  # 如果有 PID 则 kill 这些进程
  if [ ! -z "$pids" ]; then
    for pid in $pids; do
      echo "Killing process $pid using file $file"
      kill -9 $pid
    done
  fi
done
