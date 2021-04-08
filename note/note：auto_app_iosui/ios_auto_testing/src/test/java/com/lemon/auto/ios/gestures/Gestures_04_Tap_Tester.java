package com.lemon.auto.ios.gestures;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class Gestures_04_Tap_Tester {
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
		/**
		 * 命令 mobile: tap 备注 在指定控件或屏幕上的坐标执行点击手势 参数 element element: 控件ID（作为十六进制哈希字符串）。
		 * 如果设置 了element参数，则x、y代表的是以当前element为边界的xy轴。若未设置，则x,y代表的是以手机屏幕为边界 x
		 * x轴坐标，类型为float。强制参数 y y轴坐标，类型为float。强制参数 示例 // PHP $params =
		 * array(array('x'=>100.0, 'y'=>50.0, 'element'=>element.GetAttribute("id")));
		 * $driver->executeScript("mobile: tap", $params);
		 * 
		 */

		IOSElement btn = driver.findElementByAccessibilityId("id_cell_btn");

		Thread.sleep(2000);
		Map<String, Object> params = new HashMap<String, Object>();
//		params.put("element", btn.getId());
		params.put("x", 10.0);
		params.put("y", 10.0);
		driver.executeScript("mobile: tap", params);
		// Thread.sleep(3000);
//		driver.quit();

	}

}
