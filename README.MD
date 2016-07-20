# TFS自动填写脚本

## dependency

PyYAML
`pip install PyYAML`

email
`pip install email`

## `config.yaml` format

```yaml
auth:
    username: # your_username
    password: # your_password
url:
    server: # your_tfs_server
    find_item: # your_find_item_url
    update_item: # your_update_item_url
    query: # your_query_url
email:
    server: # stmp.xxx.com
    port: # 25
    from_addr: # your_email
    password: # your_password
    to_addr: # []
```