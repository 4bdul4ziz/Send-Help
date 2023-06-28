
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>


#define FROM "from@gmail.com"
#define TO "to@icloud.com"
#define CC "cc@gmal.com"

static const char *payload_text[] = {
    "Date: Fri, 19 May 2023 11:54:29 +1100\r\n",
    "To: " TO "\r\n",
    "From: " FROM "(Abdul\r\n",
    "Cc: " CC "Aziz\r\n",
    "Subject: utl_mail test message\r\n",
    "\r\n", /* empty line to divide headers from body, see RFC5322 */
    "The body of the message starts here.\r\n",
    "\r\n",
    "Some test text, whatever.\r\n",
    "Check RFC5322.\r\n",
    NULL};

struct upload_status
{
    int lines_read;
};

static size_t payload_source(void *ptr, size_t size, size_t nmemb, void *userp)
{
    struct upload_status *upload_ctx = (struct upload_status *)userp;
    const char *data;

    if ((size == 0) || (nmemb == 0) || ((size * nmemb) < 1))
    {
        return 0;
    }

    data = payload_text[upload_ctx->lines_read];

    if (data)
    {
        size_t len = strlen(data);
        memcpy(ptr, data, len);
        upload_ctx->lines_read++;

        return len;
    }

    return 0;
}

int main(void)
{
    CURL *curl;
    CURLcode res = CURLE_OK;
    struct curl_slist *recipients = NULL;
    struct upload_status upload_ctx;

    upload_ctx.lines_read = 0;

    curl = curl_easy_init();
    if (curl)
    {
        curl_easy_setopt(curl, CURLOPT_URL, "smtp.gmail.com");
        curl_easy_setopt(curl, CURLOPT_MAIL_FROM, FROM);

        recipients = curl_slist_append(recipients, TO);
        recipients = curl_slist_append(recipients, CC);
        curl_easy_setopt(curl, CURLOPT_MAIL_RCPT, recipients);


        curl_easy_setopt(curl, CURLOPT_READFUNCTION, payload_source);
        curl_easy_setopt(curl, CURLOPT_READDATA, &upload_ctx);
        curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);

        curl_easy_setopt(curl, CURLOPT_USERNAME, "user@gmail.com");
        curl_easy_setopt(curl, CURLOPT_PASSWORD, "pass");

        curl_easy_setopt(curl, CURLOPT_USE_SSL, CURLUSESSL_ALL);

        /* Send the message */
        res = curl_easy_perform(curl);

        /* Check for errors */
        if (res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
                    curl_easy_strerror(res));

        /* Free the list of recipients */
        curl_slist_free_all(recipients);

        curl_easy_cleanup(curl);
    }

    return (int)res;
}