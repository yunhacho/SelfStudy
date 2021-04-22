package Kafka.KafkaProducer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

import java.util.Arrays;
import java.util.Properties;


public class Consumer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 컨슈머 객체 필수 속성 정의
		Properties configs=new Properties();
		configs.put("bootstrap.servers", "127.0.0.1:9092"); // 컨슈머와 연결할 브로커 주소
		configs.put("group.id", "Kafka"); // 컨슈머 그룹
		configs.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer"); // 키 직렬화 시 Stringserializer 사용
		configs.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer"); // 값 키 직렬화 시 Stringserializer 사용
		
		// 앞선 속성 포함한 컨슈머 객체 생성
		KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(configs);
		// "test" 토픽 구독 
		consumer.subscribe(Arrays.asList("test"));
		//폴링 루프 시작
		while (true){
			ConsumerRecords<String, String> records=consumer.poll(500);
			for(ConsumerRecord<String, String> record : records) {
				String s=record.topic();
				if("test".equals(s))
					System.out.println(record.value());
				else
					throw new IllegalStateException("get message on topic" + record.topic());
			}
		}
	}

}
