    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Update User</h1>
                <p class="text-right"><a href="/">Home</a></p>
                {% with messages = get_flashed_messages() %}    
                {% if messages %}                        
                    {% for message in messages %}     
                        <p>{{message}}</p>          
                    {% endfor %}
                {% endif %}
            {% endwith %}
                <form action="/dashboard" method="post">
                  <div class="form-group">
                    <label>First Name</label>
                    <input type="text" value="{{user.first_name}}" class="form-control" placeholder="first name" name="first_name"> 
                  </div>
                  <div class="form-group">
                    <label>Last Name</label>
                    <input type="text" value="{{user.last_name}}" class="form-control" placeholder="last name" name="last_name"> 
                  </div>
                  <div class="form-group">
                    <label>Email</label>
                    <input type="text" value="{{user.email}}" class="form-control" placeholder="email" name="email"> 
                  </div>
                  <button type="submit" class="btn btn-primary">update</button>
                </form>
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control" placeholder="Password" value="password" name="password">
              </div>
                <div class="col">
                <h1>Users Magazines</h1>

                <form action="/dashboard" method="post">
<div>
    {% for magazine in magazines %}
    <tr>
        <td><a href="/show/{{ magazine.user_id }}">{{ magazine.title }}</a></td>
        <td>Added by {{magazine.first_name}}</td>
            
        <td>
{{ magazine.id }}"
{%  if session['user_id']  == magazine.user_id %}
 
                <a href="/destroy/{{ magazine.id }}">Delete</a>
{% endif %} -->
        </td>
    </tr>
    {% endfor %}
</div>
            </div>
        </div>
    </div>