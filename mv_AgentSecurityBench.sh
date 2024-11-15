#!/bin/bash

# 定义源目录和目标目录
SOURCE_DIR=.
DEST_DIR=../AgentSecurityBench

# 定义要排除的文件或文件夹列表（可以按需修改）
EXCLUDE_LIST=(
    "logs"     # 排除所有 .log 文件
    ".git"      # 排除 .git 文件夹
    ".github"      # 排除 .git 文件夹
    '.vscode'
    "result_csv"      # 排除 temp 文件夹
    "visualize"
    'mv_AgentSecurityBench.sh'
    'mv_ASB.sh'
    'pyproject.toml'
)

# 构建 rsync 的排除参数
EXCLUDE_PARAMS=""
for pattern in "${EXCLUDE_LIST[@]}"; do
    EXCLUDE_PARAMS+=" --exclude=${pattern}"
done

# 输出排除列表供参考
echo "Excluding the following files and directories:"
for pattern in "${EXCLUDE_LIST[@]}"; do
    echo "- ${pattern}"
done

# 使用 rsync 进行选择性复制
echo "Copying files from ${SOURCE_DIR} to ${DEST_DIR}..."
rsync -av ${EXCLUDE_PARAMS} "${SOURCE_DIR}/" "${DEST_DIR}/"

# 输出完成信息
echo "Copy complete!"
