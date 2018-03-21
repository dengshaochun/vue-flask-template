import request from '@/utils/request'

export function login(username, password) {
  return request({
    url: '/api/user/login',
    method: 'post',
    auth: {
      username: username,
      password: password
    }
  })
}

export function getInfo(token) {
  return request({
    url: '/api/user/info',
    method: 'get',
    auth: {
      username: token,
      password: ""
    }
  })
}

export function logout() {
  return request({
    url: '/api/user/logout',
    method: 'post'
  })
}
