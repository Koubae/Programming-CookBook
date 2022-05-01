<?php
/**
 * Simple Script to represent the SOLID principle in a real-world example
 *
 * NOTE: The code implemented here is not a production code not should be used or take for granted for
 * real world project. Here I represent a simple HTTP request / response pattern to show some SOLID principles in
 * all together in 1 script however it doesn't mean that the request / response implemented is correct, is just an example.
 *
 * This example does not cover all possible scenario where these principles can be applied but in order to give a quick
 * example and especially they are actually applicable all of them even in a small script.
 *
 * I 've added the tag (i.e  // O: Open-closed...) where the principle in that part of the code applies and why.
 * Actually there are some place missing where some of the principle are applied buy I did not add that tag to avoid noise.
 *
 * ----------------- < SOLID > -----------------
 *
 * S: Single - Responsibility
 * O: Open - Closed
 * L: Liskov Substitution
 * I: Interface Segregation
 * D: Dependency Inversion
 *
 *
 *
 * @author: Federico Bau
 * @php: 8.1
 */

declare(strict_types=1);

interface RequestInterface
{
    public function buildRequest(string $contentType): bool;
}

// S Single Responsibility This entity represents a Requests only
class Request implements RequestInterface
{
    // O: Open-closed the attributes are private therefore any child class cannot modify it
    private array $payload;
    private string $contentType;

    public function __construct(?array $payload = [])
    {
        $this->payload = $payload;
    }

    // O: Open-closed This method cannot be accessed by the class child
    private function make(): bool
    {
        // Implement the request make method
        return true;
    }

    public function buildRequest(string $contentType): bool
    {
        $this->contentType = $contentType;
        return true;
    }
}

interface RequestJsonInterface
{
    public function isJsonRequest($contentType): bool;
}

// S Single Responsibility This is a Request of type json
// O: Open-closed We extend the Request Class with new functionallity but not touch the parent class
class RequestJson extends Request implements RequestJsonInterface
{
    public const CONTENT_TYPE = 'application/json';

    public function buildRequest(string $contentType): bool
    {
        if (!$this->isJsonRequest($contentType)) {
            return false; // for JsonRequest only application/json is allowed!
        }
        $this->contentType = $contentType;
        return true;
    }

    public function isJsonRequest($contentType): bool
    {
        return $contentType !== self::CONTENT_TYPE;
    }
}

interface ResponseInterface
{
    public function getHeaders(): ?array;
    public function setHeaders(array $headers): bool;

    public function getBody(): string|array;
    public function setBody(string $body): bool;

    public function getCode(): ?int;
    public function setCode(int $code): bool;

    public function create(array $body): bool;
}

// S Single Responsibility This entity represents a Response only
class Response implements ResponseInterface
{
    protected array $header;
    protected string|array $body;
    private int $code;
    private string $contentType;

    public function __constructor(int $code, string $contentType)
    {
        $this->code = $code;
        $this->contentType = $contentType;
    }

    public function getHeaders(): array
    {
        return $this->header ?: [];
    }
    public function setHeaders(array $headers): bool
    {
        $this->header = array_merge($this->header, $headers);
        return true;
    }


    public function getBody(): string|array
    {
        return $this->body ?: '';
    }
    public function setBody(string|array $body): bool
    {
        $this->body = $body;
        return true;
    }

    public function getCode(): ?int
    {
        return $this->code ?: 200;
    }
    public function setCode(int $code): bool
    {
        $this->code = $code;
        return true;
    }

    public function getContentType(): ?string
    {
        return $this->contentType ?: '';
    }
    public function setContentType(string $code): bool
    {
        $this->contentType = $code;
        return true;
    }


    public function create(array $body): bool
    {
        $this->setBody($body);
        return true;
    }
}

interface ResponseHtmlInterface
{
    public function Htmlize(): void;
}

// S Single Responsibility This entity represents a Response of type html
// O: Open-closed Extend with HTML functionality
class ResponseHtml extends Response implements ResponseHtmlInterface
{
    public function create(array $body): bool
    {
        parent::create($body);
        $this->Htmlize();
        return true;
    }

    /** Just an example..
     * @return void
     */
    public function Htmlize(): void
    {
        if (is_array($this->body) ) {
            $body = implode('<br/>', $this->body);
            $this->body = "<div> {$body} </div>";
        } else {
            $this->body = "<div> {$this->body} </div>";
        }
    }
}

interface ResponseJsonInterface
{
    public function Jsonalize(): void;
}

// S Single Responsibility This entity represents a Response of type json
// O: Open-closed Extend with JSON functionality
class ResponseJson extends Response implements ResponseJsonInterface
{
    public function create(array $body): bool
    {
        parent::create($body);
        $this->Jsonalize();
        return true;
    }

    /** Just an example..
     * @return void
     */
    public function Jsonalize(): void
    {
        $this->body = json_encode(['body' => $this->body]);
    }
}


interface Http
{
    public function request(string $contentType, ?array $payload): RequestInterface;
    public function response(int $code, string $type): ResponseInterface;

}
// S Single Responsibility This entity is a base of the HTTP Request/Reponse protocol
abstract class HttpBase implements Http
{
    public const HTTP_OK = 200;
    public const HTTP_NOT_FOUND = 404;
    public const HTTP_INTERNAL_SERVER_ERROR = 500;

    public function request(string $contentType, $payload = []): \RequestInterface
    {
        switch ($contentType) {
            // L Liskov Substitution : Here we could use any of the Request' classes without changing the funcionallity of the software
            case 'application/json':
                $request = new RequestJson($payload);
                break;
            default:
                $request = new Request($payload);
        }
        return $request;
    }

    public function response(int $code, string $type): ResponseInterface
    {
        // L Liskov Substitution : Here we could use any of the Response' classes without changing the funcionallity of the software
        switch ($type) {
            case 'json':
                return new \ResponseJson($code, $type);
            case 'html':
                return new \ResponseHtml($code, $type);
            default:
                return new \Response($code, $type);
        }
    }
}

// I: Interface segregation
interface HttpConnectionInterface
{
    public function httpInit(string $requestType): bool;
}
// I: Interface segregation
interface HttpConnectionResponseInterface
{
    public function httpBuildResponse(string $responseType): void;
    public function responseContent(): string|array;
}
// I: Interface segregation
interface HttpConnectionUtilsInterface
{
    public function logPayload(): void;
}

// S Single Responsibility This class is the actual implementation of the HTTP request  / response
// O: Open-closed Extend with HTTP functionality
// I: Interface segregation we split different interfeces in specific one
class HttpConnection extends HttpBase implements
    HttpConnectionInterface,
    HttpConnectionResponseInterface,
    HttpConnectionUtilsInterface
{
    private \RequestInterface $request; // D  Dependency Inversion: Use the interface as type and not the class
    private \ResponseInterface $response; // D  Dependency Inversion: Use the interface as type and not the class

    protected array $payload;

    public function __construct(array $payload)
    {
        $this->payload = $payload;
    }

    public function httpInit(string $requestType): bool
    {
        $this->request = $this->request($requestType, $this->payload);
        return true;
    }

    public function httpBuildResponse(string $responseType): void
    {
        $response = $this->response(200, $responseType);
        $response->create($this->payload);
        $this->response = $response;
    }

    public function responseContent(): string|array
    {
        return $this->response->getBody();
    }


    public function logPayload(): void
    {
        // log the received paylod
        $dt = date("m.d.y G:i:s");
        echo "-------------------- < Payload Received at $dt  > --------------------".PHP_EOL;
        foreach($this->payload as $name => $value) {
            echo "Received $name: $value".PHP_EOL;
        }

    }
}

// S Single Responsibility This class is the actual entity used to comunicate with our software. Therefore we only care to call this class an nothing else
final class Api extends HttpConnection
{
    // O: Open-closed We extend the parent with __invoke which will use the paren'ts method untouched
    public function __invoke(string $requestType, string $responseType): mixed
    {
        $this->logPayload();
        $this->httpInit($requestType);
        // do something here...

        $this->httpBuildResponse($responseType);
        return $this->responseContent();
    }
}

$payload = [
    'param1' => 'some value',
    'param2' => 1,
    'param3' => 'more values ...'
];
$api = new Api($payload);

// JSON
var_dump($api(requestType: 'json', responseType: 'json'));
echo "*****".PHP_EOL;
var_dump($api(requestType: 'html', responseType: 'json'));

// HTML
var_dump($api(requestType: 'html', responseType: 'html'));
echo "*****".PHP_EOL;
var_dump($api(requestType: 'html', responseType: 'html'));

// Something else
var_dump($api(requestType: 'text', responseType: 'form'));