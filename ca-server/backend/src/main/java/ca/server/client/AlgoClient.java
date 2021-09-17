package ca.server.client;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.apache.http.*;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.*;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.*;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.*;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;

import static org.apache.http.entity.ContentType.APPLICATION_JSON;


public class AlgoClient {
    private String hostUrl = "";
    private CloseableHttpClient httpClient;
    private int port;

    public AlgoClient(String url, int port){
        this.hostUrl = url;
        this.port = port;
        this.httpClient = HttpClientBuilder.create().build();
    }

    public Object get(String relativePath, HashMap<String, String> params) {
        URI uri = null;
        try {
            List<NameValuePair> param = new ArrayList<>();
            for(String key : params.keySet()){
                param.add(new BasicNameValuePair(key, params.get(key)));
            }

            uri = new URIBuilder().setScheme("http").setHost(hostUrl)
                    .setPort(port).setPath(relativePath)
                    .setParameters(param).build();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }

        HttpGet httpGet = new HttpGet(uri);
        JSONObject response = send(httpGet);
        if (response == null) {
            return null;
        }
        if (!response.containsKey("data")) {
            System.out.println("Error: " + response.toJSONString());
            return null;
        }
        return response.get("data");
    }

    public Object post(String relativePath, HashMap<String, Object> data){
        data.values().removeIf(Objects::isNull);
        URI uri = null;
        try {
            uri = new URIBuilder().setScheme("http").setHost(hostUrl)
                    .setPort(port).setPath(relativePath).build();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        HttpPost httpUriRequest = new HttpPost(uri);
        String bodyString = new JSONObject(data).toJSONString();
        HttpEntity body = new StringEntity(bodyString, APPLICATION_JSON);
        httpUriRequest.setEntity(body);
        JSONObject response = send(httpUriRequest);
        if(response == null || !response.containsKey("data"))
            return null;
        return response.get("data");
    }

    private JSONObject send(HttpRequestBase requestBase){
        CloseableHttpResponse response = null;
        try {
            // 配置信息
            RequestConfig requestConfig = RequestConfig.custom()
                    .setConnectTimeout(5000)
                    .setConnectionRequestTimeout(5000)
                    .setSocketTimeout(5000)
                    .setRedirectsEnabled(true).build();
            // 将上面的配置信息 运用到这个Get请求里
            requestBase.setConfig(requestConfig);
            // 由客户端执行(发送)Get请求
            response = httpClient.execute(requestBase);
            // 从响应模型中获取响应实体
            JSONObject result = JSON.parseObject(EntityUtils.toString(response.getEntity()));
            return result;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
