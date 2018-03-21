import request from '@/utils/request'

export function getList(token) {
  return request({
    url: '/api/table/list',
    method: 'get',
    auth: {
      username: token,
      password: ""
    }
  })
}
