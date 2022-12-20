# Trajectory
DeepSORT-OSNetで追跡した物体を画像上にプロットします．
12/13:bytetrackにも対応させました

# Usage
```
python plot.py /
    --text # YOLOの検知結果を格納したテキストファイルのパスを指定する．/
    --image # 追跡した動画のサムネイルを指定する．/
    --plot # 描画形式(scatter, rectangle, line)/
    --output #出力イメージの名前/
    --model #トラッキングモデルの指定　(deepsort,bytetrack)/
    --point_size #点の大きさ(default=100, 歩行者の時は 1 でちょうどいい)/
```