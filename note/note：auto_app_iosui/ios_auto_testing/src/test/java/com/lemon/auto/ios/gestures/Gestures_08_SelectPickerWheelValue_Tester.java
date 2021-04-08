package com.lemon.auto.ios.gestures;

import java.net.URL;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Point;
import org.openqa.selenium.Rectangle;
import org.openqa.selenium.ScreenOrientation;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.internal.Yaml;

import io.appium.java_client.appmanagement.ApplicationState;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

/**
 * 		命令
		mobile: selectPickerWheelValue
		备注
		选择下一个或上一个picker wheel的值。 如果这些值是动态的，那么这个方法是能起作用的。XCTest有一个BUG就是你并不能知道要选择哪一个或者当前的选择区域是否生效
		参数
		element 
		PickerWheel的内部元素id（作为十六进制哈希字符串）执行值选择。元素必须是XCUIElementTypePickerWheel类型。必需参数
		order 
		next 选择下一个value，previous选择前面一个value。必需参数
		offset
		区间值： [0.01, 0.5]。它定义了picker wheel的中心距离应该有多远。 通过将该值乘以实际的picker wheel高度来确定实际距离。太小的偏移值可能不会改变picker wheel的值，而过高的值可能会导致picker wheel同时切换两个或多个值。通常最优值位于范围[0.15,0.3]中。默认为0.2
		示例
		// Java 
		JavascriptExecutor js = (JavascriptExecutor) driver; 
		Map<String, Object> params = new HashMap<>(); 
		params.put("order", "next"); 
		params.put("offset", 0.15); 
		params.put("element", ((RemoteWebElement) element).getId());
		js.executeScript("mobile: selectPickerWheelValue", params); 

 * @author happy
 *
 */
public class Gestures_08_SelectPickerWheelValue_Tester {
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
		
		driver.findElementByAccessibilityId("id_cell_date_picker").click();
		Thread.sleep(2000);
		
		IOSElement pickerWheel = driver.findElement(By.xpath("//XCUIElementTypeApplication[@name=\"UICatalog\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeDatePicker/XCUIElementTypeOther/XCUIElementTypePickerWheel[1]")); 

		Thread.sleep(2000);
		Map<String, Object> params= new HashMap<String, Object>();
		params.put("element", pickerWheel.getId());
		params.put("order", "next");
		params.put("offset", 0.1);
		for (int i = 0; i < 10; i++) {
			Thread.sleep(1000);
			driver.executeScript("mobile: selectPickerWheelValue", params);
		}
		

//		Thread.sleep(3000);
//		driver.quit();

	}

}
