import request from '@/utils/request'
import store from '../store'

export function login(username, password) {
  return request({
    url: '/login/',
    method: 'post',
    auth: {
      username: username,
      password: password
    }
  })
}

export function getInfo() {
  return request({
    url: '/users/' + store.getters.name + '/',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/logout/',
    method: 'post'
  })
}
