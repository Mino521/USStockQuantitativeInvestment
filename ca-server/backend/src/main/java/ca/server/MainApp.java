package ca.server;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import springfox.documentation.oas.annotations.EnableOpenApi;

@EnableOpenApi
@SpringBootApplication
@MapperScan("ca.server.mapper")
public class MainApp {

    /**
     * Application main method
     *
     * @param args the console arguments
     */
    public static void main(String[] args) {
        SpringApplication.run(MainApp.class, args);
    }
}
