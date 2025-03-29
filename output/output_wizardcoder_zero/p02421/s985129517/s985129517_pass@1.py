```python
n = int(input())
cards = [tuple(map(int, input().split())) for _ in range(n)]  # リストに変換して辞書を作らない
p_taro = p_hanako = 0
for card in cards:
    if card[0] > card[1]:   #太郎が花子に勝った時
        p_taro += 3
    elif card[0] < card[1]:
        p_hanako += 3
    else:
        p_taro += 1
        p_hanako += 1
print(p_taro, p_hanako)
```

このコードは、Pythonでデータを格納するときはデフォルトで辞書が作られるから，リストに変換して辞書ではなくても良い．
```map(int, input().split())``` の中身をtupleにすることで，入力文字列を数値に変換した上で，単純に`for`文で処理できている．

```if card[0] < card[1]:``` の判定がなくなっているところは，==を使った場合は，2番目が1の時に3を加算しなければよかった．
その他の変数も消せるかもしれない．