## 删除单条记录

## **更新一行的一个字段**

```python
POST logwarn.data.001-20200525/log/WP6qUHMBZn76WDokajUD/_update
{ "doc": { "template_id": "0" }
}
```

must

## 查询

### 查询100条、按_event_time倒排

```json
{
  "sort": {
    "_event_time": {
      "order": "desc"
    }
  },
  "from": 0,
  "size": 100
}
```

### 查询100条、按_event_time倒排、限定_event_time的范围

```json
{
  "sort": {
    "_event_time": {
      "order": "desc"
    }
  },
  "from": 0,
  "size": 100,
  "query": {
    "range": {
      "_event_time": {
        "gte": "1606292046000",
        "lt": "1606292166000"
      }
    }
  }
}
```

### 查询100条、限定_event_time的范围、按_app聚合

```json
{
  "from": 0,
  "size": 100,
  "query": {
    "range": {
      "_event_time": {
        "gte": "1606292046000",
        "lt": "1606292166000"
      }
    }
  },
  "aggs": {
    "by_app": {
      "terms": {
        "field": "_app"
      }
    }
  }
}
```

### 查询_category=兴业证券最新的10条数据

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "_category",
            "query": "兴业证券"
          }
        }
      ],
      "must_not": [],
      "should": []
    }
  },
  "from": 0,
  "size": 10,
  "sort": {
    "_event_time": {
      "order": "desc"
    }
  },
  "aggs": {}
}
```

```json
{
  "query": {
    "query_string": {
      "query": "* AND _event_time:[1607657100000 TO 1607657160000}",
      "default_field": "_message"
    }
  },
  "_source": [],
  "aggs": {
    "_category": {
      "terms": {
        "field": "_category",
        "size": 1000
      },
      "aggs": {
        "count(_application)": {
          "terms": {
            "field": "_application"
          }
        }
      }
    }
  },
  "sort": [
    {
      "_event_time": {
        "order": "desc",
        "unmapped_type": "long"
      }
    }
  ]
}
```

```json
{
  "query": {
    "query_string": {
      "query": "* AND _event_time:[1607660220000 TO 1607660280000}",
      "default_field": "_message"
    }
  },
  "_source": [],
  "aggs": {
    "_category": {
      "terms": {
        "field": "_category",
        "size": 1000
      },
      "aggs": {
        "count(_application)": {
          "terms": {
            "field": "_application"
          }
        }
      }
    }
  },
  "sort": [
    {
      "_event_time": {
        "order": "desc",
        "unmapped_type": "long"
      }
    }
  ]
}
```