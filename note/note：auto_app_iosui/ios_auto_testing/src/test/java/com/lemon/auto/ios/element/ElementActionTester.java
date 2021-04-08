package com.lemon.auto.ios.element;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.ScreenOrientation;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.internal.Yaml;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class ElementActionTester {
	/**
	 * mac osx：10.14 appium：v.12.1 xcode：10.1 iOS:12.1
	 * 
	 * @param args
	 * @throws Exception
	 */
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

		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

		// 滚动一下页面
		Map<String, Object> params = new HashMap<String, Object>();
		params.put("direction", "down");
		driver.executeScript("mobile: scroll", params);
		// 点击cell
		driver.findElementByAccessibilityId("id_cell_text_fields").click();
		// 找到第一个输入框
		IOSElement element = driver.findElementByAccessibilityId("id_tv_default");
		// 1：单击元素的中心位置：元素没有被其他元素遮挡、元素是可见的，是enable状态 ：否则报不可交互的异常
		element.click();

		// 2：输入内容：有些版本可能会比较慢
//		element.sendKeys("123456");
		element.setValue("abcdef");

		// 3:清空内容
		Thread.sleep(3000);
		element.clear();

		// 4:summit：提交Form表单元素,提交命令也可以应用于表单元素的后代元素(仅适用于Web)
//		element.submit();

		Thread.sleep(3000);
		driver.quit();

	}

}
