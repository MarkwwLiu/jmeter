import subprocess

# Python 召喚 JMeter：給你的性能測試增添一點超級英雄色彩！
def generate_html_report(test_plan_path, report_output_path):
    jmeter_cmd = "/opt/homebrew/Cellar/jmeter/5.6.3/bin/jmeter"
    jmeter_args = [
        "-n",  # Non-GUI mode
        "-t", test_plan_path,  # Path to the JMeter test plan file
        "-l", report_output_path,  # Path to save the test results
        "-e",  # Export the results in the form of an HTML dashboard report
        "-o", "/Users/markliu/Documents/html_report"  # Path to save the HTML report
    ]
    # Run JMeter test plan using subprocess
    try:
        subprocess.run([jmeter_cmd] + jmeter_args, check=True)
        print("HTML report generated successfully.")
    except subprocess.CalledProcessError as e:
        print("Error occurred while generating HTML report:", e)

# 示例用法
test_plan_path = "/Users/markliu/Documents/BitoPro.jmx"
html_report_output_path = "/Users/markliu/Documents/test_results.jtl"
generate_html_report(test_plan_path, html_report_output_path)
