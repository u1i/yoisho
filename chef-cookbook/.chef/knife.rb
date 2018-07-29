# See http://docs.chef.io/config_rb_knife.html for more information on knife configuration options

current_dir = File.dirname(__FILE__)
log_level                :info
log_location             STDOUT
node_name                "u1i"
client_key               "#{current_dir}/u1i.pem"
chef_server_url          "https://api.chef.io/organizations/sotong"
cookbook_path            ['.', '..', './cookbooks', "#{current_dir}/../chef-cookbook"]
