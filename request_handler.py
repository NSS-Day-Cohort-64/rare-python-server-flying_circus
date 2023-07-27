from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse #, parse_qs
from views import (create_user, login_user, get_all_users, get_single_user,
get_all_tags,
get_all_subscriptions,
get_all_reactions,
get_all_posts, get_single_post, create_post,
get_all_post_reactions,
get_all_comments,
get_all_categories,
get_all_post_tags, get_posts_by_user, create_category)


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]
        if '?' in path:
            # param = resource.split('?')[1]
            # resource = resource.split('?')[0]
            pair = parsed_url.query.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        parsed = self.parse_url(self.path)

        response = False

        if '?' not in self.path:
            # unpack tuple
            ( resource, id ) = parsed

            if resource == "users":
                if id is not None:
                    response = get_single_user(id)
                else:
                    response = get_all_users()

            elif resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()

            elif resource == "comments":
                response = get_all_comments()

            elif resource == "tags":
                response = get_all_tags()

            elif resource == "categories":
                response = get_all_categories()

            elif resource == "subscriptions":
                response = get_all_subscriptions()

            elif resource == "reactions":
                response = get_all_reactions()

            elif resource == "post_reactions":
                response = get_all_post_reactions()

            elif resource == "post_tags":
                response = get_all_post_tags()

        else:
            ( resource, key, value ) = parsed
            if key == 'user' and resource == 'posts':
                response = get_posts_by_user(value)

        self._set_headers(200)

        self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        (resource, _) = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'categories':
            response = create_category(post_body)
        if resource == 'posts':
            response = create_post(post_body)

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        pass

    def do_DELETE(self):
        """Handle DELETE Requests"""
        pass


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
