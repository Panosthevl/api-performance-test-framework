import http from 'k6/http';
import {check,sleep} from 'k6';

export const options={
    stages:[
        {duration:'10s',target:15},
        {duration:'20s',target:30},
        {duration:'10s',target:10}
    ],
    thresholds:{
        http_req_failed:['rate<0.02'],
        http_req_duration:['p(95)<3000'],// when the metric is below 2000 is crossed.
    },
};

export default function(){
    const res = http.get('https://reqres.in')

    check(res,{
        'status is 200': (r) => r.status === 200.
    });
    sleep(1);
}