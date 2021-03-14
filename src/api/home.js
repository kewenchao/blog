import request from '../network/request'
/**
 * getHome() 文章列表请求
 */
export function getHome() {
    return request({
        url: "/post"
    })
}

// 文章详情
export function getPost(postId) {
    return request({
        url: `/post/${postId}`
    })
}

// 发起评论
export function postComment(postId, author, content) {
    return request({
        url: "/comment",
        method: "post",
        data: {
            post_id: postId,
            author,
            content
        }
    })
}
