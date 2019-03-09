#
# class Class
#   alias old_new new
#   def new(*args)
#     print "Creating a new ", self.name, "\n"
#     old_new(*args)
#   end
# end
class Inventory
  def extract_ipv4(line)
    ip_regex=/(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/
    ip=line[ip_regex]
    return ip
  end
  def get_hostname(line)
    return line.split[0]
  end

  #return a dict with all groups passed in
  def get_hosts_by_groups(group_list)

      inventory={}
      for group in group_list do
          inventory[group]=@inventory[group]
      end
      return inventory
  end
  def initialize(file_path="./vagrant_hosts")

      File.open(file_path, "r") do |f|
          dictionary={}
          first_group_found=false
          curr_dict={}
          array_item=[]
          f.each_line do |line|

              is_group=  /\[.*\]/=~line

              if first_group_found!=true and is_group then
                  #find the first group
                  first_group_found=true
                  idx=line.strip.delete("[]")

                  curr_dict[idx]=array_item
              elsif is_group then
                  dictionary=dictionary.merge(curr_dict)

                  curr_dict={}
                  array_item=[]
                  idx=line.strip.delete("[]")
                  curr_dict[idx]=array_item
              else

                  ipv4 =extract_ipv4(line)

                  if ipv4 then
                      hostname=get_hostname(line)
                      array_item.push({hostname:hostname,ipv4:ipv4})
                  end
              end
          end
          @inventory={}
          dictionary=dictionary.merge(curr_dict)
          dictionary.each do |key, value|
              if value.length>0 then
                  @inventory[key]=value
                  #puts (key + "\n\t-->" + value*",")
              end
          end

      end
  end

end
