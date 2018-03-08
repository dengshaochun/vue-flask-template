import request from '@/utils/request'

export function getList(token) {
  return request({
    url: '/api/table/list',
    method: 'get',
    params: { token }
  })
}
