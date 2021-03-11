// 首页需要请求的接口


import request  from '../network/request'
export function getHome(){
    request({
        url: "/post"
    }).then((result) => {
        console.log(result);
    }).catch((err) => {
        console.log(err)
    });
}
