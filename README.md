# jieba-zh_TW

結巴(jieba)斷詞台灣繁體版本


## 與各版本的差異說明

ldkrsi 版本：採用和原始jieba相同的演算法，替換其詞庫及HMM機率表製做出針對台灣繁體的jieba斷詞器

leafwind 版本：沿用同樣繁體詞庫以及 HMM 機率表，並增加 `setup.py`，再更改資料夾結構，讓使用上更容易




## 使用說明

* 相容python2和python3

### 安裝

#### 直接使用 pip install 安裝

```
pip install https://github.com/leafwind/jieba-zh_TW.git#egg=jieba_zh_tw
)
```

#### 或寫在 `requirements.txt`

```
-e git+https://github.com/leafwind/jieba-zh_TW.git#egg=jieba_zh_tw
```

### import

### 直接 import

- `import jieba_zh_tw as jieba`

### 同時 import 簡體與正體版本

```
import jieba  # 原始簡體中文版 jieba
import jieba_zh_tw as jiebatw  # 正體中文版 jieba
```

## 程式碼範例

操作方法同原始jieba

### 斷詞

```python
import jieba

#如果您的電腦同時要使用兩個版本的jieba，請自訂cache檔名，避免兩個cache互相蓋住對方
#jieba.dt.cache_file = 'jieba.cache.new'

seg_list = jieba.cut("在非洲，每六十秒，就有一分鐘過去") 
print("|".join(seg_list))
# 在|非洲|，|每|六十秒|，|就|有|一分鐘|過去

```

### 關鍵詞抽取
尚未替換機率表，輸出的結果非常不可靠


### 詞性標記
應該是一跑就會噴錯的狀態


## 可靠度探討
拿本份程式碼去和*jieba轉簡體後斷詞*、*jieba直接斷繁體字*這兩個方法，去斷[這篇台灣記者寫的新聞](http://www.appledaily.com.tw/appledaily/article/international/20160715/37308809/)。並以[中研院中文斷詞系統](http://ckipsvr.iis.sinica.edu.tw/)作為標準答案，以詞為單位，去計算這三個方法和中研院的結果的[Edit distance](https://en.wikipedia.org/wiki/Edit_distance)


|Edit distance|第一段(92)|第二段(136)|第三段(75)|第四段(52)|第五段(63)|
|---|---|---|---|---|---|
|jieba zh_TW      |9|20|12|12|9|
|jieba轉簡體後斷詞|44|43|31|23|21|
|jieba直接斷繁體字|53|74|43|34|34|
(括號內為中研院斷出來的詞彙數)


## 感謝

* 中央研究院資訊科學所詞庫小組中文斷詞線上服務

## 注意事項

使用本份程式碼請遵守[中研院斷詞服務之服務條款](http://ckipsvr.iis.sinica.edu.tw/terms.htm)其中的衍生資料相關規定

