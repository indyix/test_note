package com.lemon.auto.ios.concept;

import java.util.HashMap;
import java.util.Map;

import org.apache.http.HttpHost;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import com.alibaba.fastjson.JSONObject;

/**
 * {
  "deviceName": "iPhone 8",
  "platformVersion": "13.1",
  "platformName": "iOS",
  "app": "/Users/nick/Desktop/tools/app/UICatalog.app"
}
 * @author Happy
 *
 */
public class ConceptTester {

	public static void main(String[] args) throws Exception {
	
		//创建会话的url
		String url = "http://localhost:4723/wd/hub/session";
		//创建一个post请求
		HttpPost createSession = new HttpPost(url);
		//指定一个代理
		HttpHost host = new HttpHost("127.0.0.1", 8888, "http");
		//创建一个请求配置
		RequestConfig config = RequestConfig.custom().setProxy(host).build();
		//设置请求配置
		createSession.setConfig(config);
		//创建一个请求体
		Map<String, Object> map = new HashMap<String, Object>();
		map.put("platformName", "iOS");
		map.put("platformVersion", "13.1");
		map.put("deviceName", "iPhone 8");
		map.put("app", "/Users/nick/Desktop/tools/app/UICatalog.app");
		map.put("automationName", "XCUITest");
		//组装成一个json字符串
		String jsonParams = "{\"desiredCapabilities\":"+ JSONObject.toJSONString(map) +"}";
		StringEntity entity = new StringEntity(jsonParams, ContentType.APPLICATION_JSON);
		//设置请求体
		createSession.setEntity(entity);
		//发包客户端
		CloseableHttpClient httpClient = HttpClients.createDefault();
		//发包
		CloseableHttpResponse response = httpClient.execute(createSession);
		//输出响应体
		System.out.println(EntityUtils.toString(response.getEntity()));
		
	}

}
