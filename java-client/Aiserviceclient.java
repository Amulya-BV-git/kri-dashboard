import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.client.SimpleClientHttpRequestFactory;

public class AiServiceClient {

    private RestTemplate restTemplate;

    public AiServiceClient() {
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setConnectTimeout(10000);
        factory.setReadTimeout(10000);

        this.restTemplate = new RestTemplate(factory);
    }

    public String callTest(String url, String json) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<String> request = new HttpEntity<>(json, headers);

            ResponseEntity<String> response =
                    restTemplate.postForEntity(url + "/test", request, String.class);

            return response.getBody();

        } catch (Exception e) {
            return null;
        }
    }

    public String callGenerate(String url, String json, String token) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            headers.set("Authorization", "Bearer " + token);

            HttpEntity<String> request = new HttpEntity<>(json, headers);

            ResponseEntity<String> response =
                    restTemplate.postForEntity(url + "/generate-report", request, String.class);

            return response.getBody();

        } catch (Exception e) {
            return null;
        }
    }
}