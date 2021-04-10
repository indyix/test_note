package com.lemon.auto.ios.web;

import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class HybirdTester3 {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "12.1");
		// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/happy/Desktop/tools/app/UICatalog.app");
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 是否重置app设置
		desiredCapabilities.setCapability("noReset", true);
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		// 滑动到底部
		Map<String, Object> params= new HashMap<String, Object>();
		params.put("direction", "up");
		driver.executeScript("mobile: swipe", params);
		
		//点击web view
		driver.findElementByAccessibilityId("id_cell_web_view").click();
		Thread.sleep(5000);
		Set<String> handleSet = driver.getContextHandles();
		//转换成有序的列表
		ArrayList<String> handleList = new ArrayList<String>(handleSet);
		//获得web的上下文字符串
		String webContext = handleList.get(1);
		//1:切换到web上下文
		driver.context(webContext);
		System.out.println("--------------第一次切换后---------------");
		//是否为浏览器
		System.out.println(driver.isBrowser());//true
		//获取当前的上下文
		System.out.println(driver.getContext());//WEBVIEW_7107.1
		//获取可用的自动化的上下文
		System.out.println(driver.getContextHandles());
		
		//采用webdriver的api--》web自动化测试
		driver.findElementByPartialLinkText("Buy").click();
		
		Thread.sleep(3000);
		//2:切换为原生app上下文
		driver.context(handleList.get(0));
		//点击导航条上的返回按钮（特别注意！！！先切换原生app上下文，才能对原生控件操作）
		driver.findElement(By.xpath("//XCUIElementTypeButton[@name=\"UICatalog\"]")).click();
		System.out.println("--------------第二次切换后---------------");
		//是否为浏览器
		System.out.println(driver.isBrowser());//
		//获取当前的上下文
		System.out.println(driver.getContext());//
		//获取可用的自动化的上下文
		System.out.println(driver.getContextHandles());
		
		Thread.sleep(3000);
		// 滑动到顶部
		Map<String, Object> params2= new HashMap<String, Object>();
		params2.put("direction", "down");
		driver.executeScript("mobile: swipe", params2);
		
		//点击action sheet
		driver.findElementByAccessibilityId("id_cell_action_sheet").click();
		
//		Thread.sleep(3000);
//		driver.quit();

	}

}
