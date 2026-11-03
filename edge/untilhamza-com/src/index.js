// untilhamza.com edge: proxy the GitHub Pages build, keep the browser on
// untilhamza.com. www.untilhamza.com 308s to the bare domain.
const CANONICAL_HOST = "untilhamza.com";
const ORIGIN = "https://untilhamza.github.io";
const ORIGIN_HOST = "untilhamza.github.io";
const REWRITE_TYPES = /text\/html|text\/xml|application\/xml|application\/rss|application\/atom|application\/json|text\/plain/;

export default {
  async fetch(request) {
    const url = new URL(request.url);

    if (url.hostname !== CANONICAL_HOST || url.protocol !== "https:") {
      url.hostname = CANONICAL_HOST;
      url.protocol = "https:";
      return Response.redirect(url.toString(), 308);
    }

    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method Not Allowed", { status: 405, headers: { allow: "GET, HEAD" } });
    }

    const upstream = await fetch(ORIGIN + url.pathname + url.search, {
      method: request.method,
      headers: { accept: request.headers.get("accept") ?? "*/*" },
      redirect: "manual",
      cf: { cacheTtl: 300, cacheEverything: true },
    });

    const headers = new Headers(upstream.headers);
    const location = headers.get("location");
    if (location) {
      headers.set("location", location.replace(`https://${ORIGIN_HOST}`, `https://${CANONICAL_HOST}`).replace(`http://${ORIGIN_HOST}`, `https://${CANONICAL_HOST}`));
    }
    headers.set("x-served-by", "untilhamza-com-edge");

    const type = headers.get("content-type") ?? "";
    if (request.method === "GET" && REWRITE_TYPES.test(type) && upstream.body) {
      const text = await upstream.text();
      headers.delete("content-length");
      return new Response(text.replaceAll(`https://${ORIGIN_HOST}`, `https://${CANONICAL_HOST}`).replaceAll(`http://${ORIGIN_HOST}`, `https://${CANONICAL_HOST}`), {
        status: upstream.status,
        headers,
      });
    }

    return new Response(upstream.body, { status: upstream.status, headers });
  },
};
