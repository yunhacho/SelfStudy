package Kafka.KafkaProducer;
import java.io.IOException;
import java.util.Properties;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

// 특정 토픽에 레코드 생성하는 프로듀서 클래스 
public class Producer {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		// 프로듀서 객체 필수 속성 정의 
		Properties configs=new Properties();
		configs.put("bootstrap.servers", "127.0.0.1:9092"); // 프로듀서가 최초로 연결할 브로커 주소
		configs.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer"); // 키 직렬화 시 Stringserializer 사용
		configs.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer"); // 값 직렬화 시 Stringserializer 사용
		
		// 앞선 속성을 토대로 카프카 프로듀서 객체 생성
		KafkaProducer<String, String> producer=new KafkaProducer<String, String>(configs);
		
		for(int i=0; i<5; i++) {
			String message="hello it is line "+i;
			// "test" 토픽에 message 값 갖는 ProducerRecord를 브로커에 전송
 			producer.send(new ProducerRecord<String, String>("test", message));
			System.out.println("done");
		}
		
		// 프로듀서 객체 닫기
		producer.flush();
		producer.close();
	}

}
