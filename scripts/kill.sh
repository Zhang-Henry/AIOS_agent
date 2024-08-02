pids=$(ps -ef | grep main_attacker | grep -v grep | awk '{print $2}')

# 检查是否找到任何进程
if [ -z "$pids" ]; then
  echo "没有找到与 main_attacker 相关的进程。"
else
  # 终止所有找到的进程
  for pid in $pids; do
    echo "终止进程 $pid"
    kill -9 $pid
  done
  echo "所有与 main_attacker 相关的进程已终止。"
fi