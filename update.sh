#!/bin/sh

currentVersion="$(cat postman.spec | grep Version: | awk '{print $2}')"
currentBuildId="$(cat postman.spec | grep '%global build_id' | awk '{print $3}')"

apiResponse="$(curl -s 'https://www.postman.com/mkapi/release.json')"
latestVersion="$(printf "%s" "${apiResponse}" | jq -r '.notes[0].version')"
latestBuildId="$(latestVersion)"

echo "Current version: $currentVersion build: $currentBuildId"
echo "Latest version: $latestVersion build: $latestBuildId"


if [ "$currentBuildId" != "$latestBuildId" ]; then
	DATE="$(date "+%a %b %d %Y")"
	USER="RPM Bot <rpm-bot@coder966.net>"


	sed -i "s/^Version: .*/Version:       ${latestVersion}/" postman.spec
	sed -i "s/^%global *build_id .*/%global build_id ${latestBuildId}/" postman.spec
	sed -i "s/^%changelog/%changelog\n\* ${DATE} ${USER} - ${latestVersion}\n- Update to ${latestVersion}\n/" postman.spec


	git commit postman.spec -m "Update to ${latestVersion}"
	git push
fi
