#!/bin/bash

# URLの一覧を配列に設定
urls=("https://www.bucherer.com/rolex-certified-pre-owned/watches/turn-o-graph/1404-824-3.html"
      "https://www.bucherer.com/rolex-certified-pre-owned/watches/turn-o-graph/1404-824-3.html"
      "https://www.bucherer.com/rolex-certified-pre-owned/watches/day-date/1403-959-3.html")

for url in "${urls[@]}"; do
    echo "Processing URL: $url"
    curl -s "$url" | grep "brb-product__detail-specs__value"
done