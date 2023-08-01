from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
from views import (create_user, login_user, get_all_users, get_single_user,
get_all_tags, create_tag,
get_all_subscriptions,
get_all_reactions,
get_all_posts, get_single_post, get_posts_by_category, get_posts_by_title, get_posts_by_tag, create_post,
get_all_post_reactions,
get_all_comments,
get_all_categories,
get_all_post_tags, get_posts_by_user, create_category, delete_post, update_post,
create_subscription, create_multiple_post_tags, delete_multiple_post_tags)


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""
    # def parse_url(self, path):
    #     """Parse the url into the resource and id"""
    #     parsed_url = urlparse(path)
    #     path_params = parsed_url.path.split('/')
    #     resource = path_params[1]
    #     if '?' in path:
    #         # param = resource.split('?')[1]
    #         # resource = resource.split('?')[0]
    #         pair = parsed_url.query.split('=')
    #         key = pair[0]
    #         value = pair[1]
    #         return (resource, key, value)
    #     else:
    #         id = None
    #         try:
    #             id = int(path_params[2])
    #         except (IndexError, ValueError):
    #             pass
    #         return (resource, id)
    
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

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
            ( resource, query ) = parsed
            
            if resource == 'posts':
                if query.get('user'):
                    response = get_posts_by_user(query['user'][0])
                elif query.get('category'):
                    response = get_posts_by_category(query['category'][0])
                elif query.get('title'):
                    response = get_posts_by_title(query['title'][0])
                elif query.get('tag'):
                    response = get_posts_by_tag(query['tag'][0])
                
                    
            # ( resource, key, value ) = parsed
            # if resource == 'posts':
            #     if key == 'user':
            #         response = get_posts_by_user(value)
            #     if key == "category":
            #         response = get_posts_by_category(value)

        self._set_headers(200)

        self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
        """Make a post request to the server"""
        status_code = 201
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
        if resource == 'tags':
            response = create_tag(post_body)
        if resource == 'post_tags':
            if (
                isinstance(post_body, list)
                and len(post_body) == 2
                and isinstance(post_body[0], int)
                and isinstance(post_body[1], list)
            ):
                response = create_multiple_post_tags(post_body)
            else:
                status_code = 400
                response = json.dumps({
                    "required_format": ["post_id", ["tag_id_1", "tag_id_2", "etc"]]
                    })
        elif resource == 'subscriptions':
            response = create_subscription(post_body)

        self._set_headers(status_code)

        self.wfile.write(response.encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "posts":
            success = update_post(id, post_body)
        
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())
     

    def do_DELETE(self):
        """Handle DELETE Requests"""
        delete_body = None
        content_len = int(self.headers.get('content-length', 0))
        if content_len > 0:
            delete_body = json.loads(self.rfile.read(content_len))

        status_code = 204
        response = ""
        (resource, id) = self.parse_url(self.path)

        if resource == "posts":
            delete_post(id)
        if resource == "post_tags+bulk_delete":
            if (
                delete_body is not None
                and isinstance(delete_body, list)
                and len(delete_body) > 0
                and isinstance(delete_body[0], int)
            ):
                delete_multiple_post_tags(delete_body)
            else:
                status_code = 400
                response = json.dumps({
                    "error - bad request": """To  perform a bulk delete operation of post_tags, 
                    please provide an array of the primary keys you would like to delete""",
                    "example": [8, 9, 10]
                    })

        self._set_headers(status_code)
        self.wfile.write(response.encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
