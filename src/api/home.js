import request  from '../network/request'
/**
 * getHome() 文章列表请求
 */
export function getHome(){
    return request({
        url: "/post"
    })
}

export function getPost(postId){
    return request({
        url: `/post/${postId}`
    })
}

