
module Inventory
  def Inventory.extract_ipv4(line)
    ip_regex=/(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/
    ip=line[ip_regex]
    return ip
  end
  def Inventory.get_hostname(line)
    first_word_regex=/([a-z].*) /
    hostname=line[first_word_regex]
    return hostname
  end
  def Inventory.read_file(file_path="vagrant_hosts")

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
          inventory={}
          dictionary=dictionary.merge(curr_dict)
          dictionary.each do |key, value|
              if value.length>0 then
                  inventory[key]=value
                  #puts (key + "\n\t-->" + value*",")
              end
          end
          return inventory
      end
  end

end
