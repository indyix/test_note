package com.lemon.auto.ios.gestures;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class Gestures_05_DoubleTap_Tester {
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

		IOSElement btn = driver.findElementByAccessibilityId("id_cell_btn");

		Thread.sleep(2000);
		Map<String, Object> params = new HashMap<String, Object>();
//		params.put("element", btn.getId());
		params.put("x", 10.0);
		params.put("y", 10.0);
		driver.executeScript("mobile: doubleTap", params);
		// Thread.sleep(3000);
//		driver.quit();

	}

}
